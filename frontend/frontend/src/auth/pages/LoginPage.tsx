import LoginForm from '../components/LoginForm';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import addItemImage from '../../assets/add_item.png';
import itemList from '../../assets/item_list.png';
import searchItemList from '../../assets/search_item_list.png';

const LoginPage = () => {
  return (
    <div className="py-20 md:py-10">
      <div className="w-5/6 md:w-1/2 bg-primary-foreground mx-auto">
        <Card>
          <CardHeader>
            <CardTitle className="font-bold">Welcome back</CardTitle>
            <CardDescription>Let&apos;s get you signed in.</CardDescription>
          </CardHeader>
          <CardContent>
              <LoginForm />
          </CardContent>
          <CardContent>
            <p>Not sure? Keep reading...</p>
          </CardContent>
          <CardContent>
            <h3 className="font-extrabold">Yours.</h3>
            <p>
              Create your inventory.
            </p>
            <img src={addItemImage} alt="Screenshot" />
          </CardContent>
          <CardContent className="before:border-e-red-950">
            <h3 className="font-extrabold">See.</h3>
            <p>
            Keep track of everything.
            </p>
            <img src={itemList} alt="Screenshot" />
          </CardContent>
          <CardContent className="before:border-e-red-950">
            <h3 className="font-extrabold">Search.</h3>
            <p>
              Find everything easily.
            </p>
            <img src={searchItemList} alt="Screenshot" />
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default LoginPage;
